import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-3.025, 3.2).lineTo(3.025, 3.2).lineTo(3.025, -3.2).lineTo(-3.025, -3.2).lineTo(-3.025, 3.2).close()
solid=wp_sketch0.add(loop0).extrude(8.661705110607995)
