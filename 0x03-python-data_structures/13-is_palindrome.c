#include "lists.h"

/**
 * is_palindrome - check if it is palindrme or not
 *
 * @head: pointer
 *
 * Return: 0 or 1
 *
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return(1);
	return (a(head, *head));
}

/**
 * a - check if it is palindrme or not
 *
 * @head: pointer
 * @e: end of the list
 *
 */

int a(listint_t **head, listint_t *e)
{
	if (e == NULL)
		return (1);
	if (a(head, e->next) && (*head)->n == e->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
