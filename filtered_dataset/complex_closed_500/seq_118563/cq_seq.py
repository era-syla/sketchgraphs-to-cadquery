import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.15, 0.0).lineTo(0.15, 0.025).lineTo(0.0, 0.025).lineTo(-0.10032, 0.11533).lineTo(-0.12113, 0.0966).lineTo(0.0, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.4174914501515709)
