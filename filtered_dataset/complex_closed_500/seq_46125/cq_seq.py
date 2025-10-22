import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.3302, -0.0).lineTo(0.3302, 0.0762).lineTo(0.1778, 0.0762).lineTo(0.1778, -0.0762).lineTo(0.3302, -0.0762).lineTo(0.3302, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.22089441357108403)
