from invoke import task


@task
def deploy(ctx):
    """ 
    Runs the deploy server. 
    """
    ctx.run('python3 manage.py makemigrations')
    ctx.run('python3 manage.py migrate')
    ctx.run('gunicorn codeschool.wsgi -b unix:///tmp/sock/webapp.sock '
            '--reload -w 4')


@task
def docker_build(ctx, rebuild_static=False):
    if rebuild_static:
        ctx.run('tar czpf static.tar.gz src/produtos_ivone/static/')
    ctx.run('docker build -f Dockerfile'
            '-t src .', pty=True)
