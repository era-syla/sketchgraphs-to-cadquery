import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-2.3, 0.025).lineTo(-0.55, 0.025).lineTo(-0.55, 1.875).lineTo(-2.3, 1.875).lineTo(-2.3, 0.025).close()
solid=wp_sketch0.add(loop0).extrude(4.909463690011753)
