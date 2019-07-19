/**
 * 
 * @authors Shanming (shanming0428@163.com)
 * @date    2019-07-12 23:21:43
 * @version $Id$
 */

import React from 'react';
import {
    List,
    Datagrid,
    TextField,
    EmailField,
    UrlField,
    BooleanField,
    ReferenceField,
    Edit,
    SimpleForm,
    DisabledInput,
    ReferenceInput,
    SelectInput,
    TextInput,
    LongTextInput,
    Create,
    BooleanInput,
    EditButton
} from 'react-admin';
import MyUrlField from './MyUrlField';


export const UserList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="name" />
            <EmailField source="email" />
            <BooleanField source="active" />
            <ReferenceField source="role_id" reference="roles">
                <TextField source="id" />
            </ReferenceField>
            <EditButton />
        </Datagrid>
    </List>
)

export const UserEdit = props => (
    <Edit {...props}>
        <SimpleForm>
           <DisabledInput source="id" />
           <DisabledInput source="name" />
           <TextInput source="email"/>
           <BooleanInput source="active" />
        </SimpleForm>
    </Edit>
);

export const UserCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <TextInput source="email"/>
            <BooleanInput source="active" />
        </SimpleForm>
    </Create>
);