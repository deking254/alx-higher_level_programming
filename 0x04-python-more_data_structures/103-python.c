#include <Python.h>
#include <stdio.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
/**
 * print_python_list - check the code
 * @p: p
 * Return: Always 0.
 */
void print_python_list(PyObject *p)
{
int j = 0;
PyListObject *lst = (PyListObject *)p;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)(p))->ob_size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (j = 0; j < ((PyVarObject *)(p))->ob_size; j++)
{
printf("Element %d: %s\n", j, lst->ob_item[j]->ob_type->tp_name);
}
if (PyBytes_Check(p))
print_python_bytes(p);
}
/**
 * print_python_bytes - check the code
 * @p: p
 * Return: Always 0.
 */
void print_python_bytes(PyObject *p)
{
int i = 0;
PyBytesObject *y = (PyBytesObject *)p;
char *arr = y->ob_sval;
printf("[.] bytes object info\n");
if (PyBytes_Check(p))
{
printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", arr);
if (((PyVarObject *)p)->ob_size < 10)
{
printf("  first %ld bytes: ", ((PyVarObject *)p)->ob_size + 1);
while (i < ((PyVarObject *)p)->ob_size + 1)
{
printf("%2.2hhx ", (unsigned int)arr[i]);
i++;
}
}
if (((PyVarObject *)p)->ob_size >= 10)
while (i < 10)
{
printf("%2.2hhx ", arr[i]);
i++;
}
printf("\n");
}
else
printf("  [ERROR] Invalid Bytes Object\n");
}
