#include "lists.h"
/**
 * insert_node - function that inserts a number into a singly linked list
 * @head: headnode
 * @number:number to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	prev->next = new;
	new->next = current;

	return (new);
}
