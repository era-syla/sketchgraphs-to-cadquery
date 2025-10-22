import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.0949).lineTo(0.025, 0.0949).lineTo(0.025, 0.03715).lineTo(0.04598, 0.01215).lineTo(0.04598, -0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.25092585570134196)
