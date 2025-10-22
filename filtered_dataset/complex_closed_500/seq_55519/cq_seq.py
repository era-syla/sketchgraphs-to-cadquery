import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02, 0.03).lineTo(0.03, 0.03).lineTo(0.03, 0.02).lineTo(0.02, 0.03).close()
solid=wp_sketch0.add(loop0).extrude(0.008779503264690404)
