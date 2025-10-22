import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.17145, 0.0).lineTo(0.17145, 0.17145).lineTo(-0.0, 0.17145).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.15514054738270752)
