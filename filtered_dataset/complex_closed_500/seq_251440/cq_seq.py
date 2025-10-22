import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0525, -0.0525).lineTo(-0.0525, -0.0525).lineTo(-0.0525, 0.0525).lineTo(0.0525, 0.0525).lineTo(0.0525, -0.0525).close()
solid=wp_sketch0.add(loop0).extrude(-0.16107553790488607)
