import React from 'react';
import { connect } from 'dva';
import styles from './HomeLayout.less';
import { Layout, Menu, Affix, Button } from 'antd';
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
} from '@ant-design/icons';

const { Header, Sider, Content, Footer } = Layout;

// 组件本身
// 所需要的数据通过 Container Component 通过 props 传递下来
class HomeLayout extends React.Component {

    state = {
        collapsed: false,
      };
    
      toggle = () => {
          this.setState({
              collapsed: !this.state.collapsed,
          });
      };

    render() {
        return (
            <Layout>
                <Sider trigger={null} collapsible collapsed={this.state.collapsed}>
                    <div className={styles.logo} />
                    <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']} className={styles.trigger}>
                        <Menu.Item key="1" icon={<UserOutlined />}>nav 1</Menu.Item>
                        <Menu.Item key="2" icon={<VideoCameraOutlined />}>nav 2</Menu.Item>
                        <Menu.Item key="3" icon={<UploadOutlined />}>nav 3</Menu.Item>
                    </Menu>
                </Sider>
                <Layout className={styles.siteLayout} >
                    <Header className={styles.siteLayoutBackground} style={{ padding: 0, }} >                       
                        {React.createElement(this.state.collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, { 
                            className: {},
                            onClick: this.toggle, 
                        })}                     
                    </Header>
                    <Content className={styles.siteLayoutBackground} style={{ margin: '24px 16px', padding: 24, minHeight: 7500, }} >
                        <div className={styles.siteLayoutContent}>Content</div>
                        
                    </Content>
                    <Footer style={{ textAlign: 'center', background: "#fff", }}>Ant Design ©2018 Created by Ant UED</Footer>
                </Layout>
            </Layout>
        );
    }
}

// export default Products;
export default connect()(HomeLayout);
