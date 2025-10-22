import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.05, -0.0525).lineTo(0.05, 0.0525).lineTo(-0.05, 0.0525).lineTo(-0.05, -0.0525).lineTo(0.05, -0.0525).close()
solid=wp_sketch0.add(loop0).extrude(-0.1583686798644775)
