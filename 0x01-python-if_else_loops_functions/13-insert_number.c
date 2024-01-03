#include "lists.h"
/**
 * insert_node - inserting number into a linked list
 * @head: pointer to the head address
 * @number: the number of node to inseart
 * Return: nod on successe or 0 if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	temp = *head;
	if (head == NULL)
		return (NULL);

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;

	if (temp == NULL || temp->n >= number)
	{
		newnode->next = temp;
		*head = newnode;
		return (newnode);
	}

	while (temp != NULL && temp->next != NULL && temp->next->n <= number)
		temp = temp->next;

	newnode->next = temp->next;
	temp->next = newnode;

	return (newnode);
}
