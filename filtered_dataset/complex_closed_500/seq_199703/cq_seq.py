import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.025, 0.025).lineTo(-0.025, 0.025).lineTo(-0.025, -0.025).lineTo(0.025, -0.025).lineTo(0.025, 0.025).close()
solid=wp_sketch0.add(loop0).extrude(0.010802766461440405)
