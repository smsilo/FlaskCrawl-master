"""empty message

Revision ID: e87c9161ec8b
Revises: 
Create Date: 2017-12-18 07:17:26.969916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e87c9161ec8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('iprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instagram_id', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('instagram_id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=130), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('max_insta_accounts', sa.Integer(), nullable=False),
    sa.Column('profile_pic', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('iprofile_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('followers_count', sa.Integer(), nullable=True),
    sa.Column('following_count', sa.Integer(), nullable=True),
    sa.Column('media_likes', sa.Integer(), nullable=True),
    sa.Column('engagement_rate', sa.Float(), nullable=True),
    sa.Column('iprofile_id', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['iprofile_id'], ['iprofile.instagram_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('iprofile_id', 'date', name='_profile_data_uc')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('users_iprofiles',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('iprofile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['iprofile_id'], ['iprofile.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_iprofiles')
    op.drop_table('roles_users')
    op.drop_table('iprofile_data')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('iprofile')
    # ### end Alembic commands ###
