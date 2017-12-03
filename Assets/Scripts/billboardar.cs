using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Lean.Touch
{
	public class billboardar : MonoBehaviour {

		SpriteRenderer rend;

		protected virtual void OnEnable()
		{
			rend = this.gameObject.GetComponent<SpriteRenderer> ();
			// Hook into the events we need
			LeanTouch.OnGesture     += OnGesture;
		}

		protected virtual void OnDisable()
		{
			// Unhook the events
			LeanTouch.OnGesture     -= OnGesture;
		}

		public void OnGesture(List<LeanFinger> fingers)
		{
			rend.enabled = false;
			rend.color = new Color(1f,1f,1f,0f);
		}
			
	}
}