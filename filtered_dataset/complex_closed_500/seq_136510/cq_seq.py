import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02234, -0.02613).lineTo(0.02634, -0.02613).lineTo(0.02634, -0.02213).lineTo(0.02234, -0.02213).lineTo(0.02234, -0.02613).close()
solid=wp_sketch0.add(loop0).extrude(0.0004941983906204505)
