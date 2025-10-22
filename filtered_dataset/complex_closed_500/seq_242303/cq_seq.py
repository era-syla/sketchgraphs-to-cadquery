import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0022, 0.03517).lineTo(-0.0022, 0.03517).lineTo(-0.0022, 0.03838).lineTo(0.0022, 0.03838).lineTo(0.0022, 0.03517).close()
solid=wp_sketch0.add(loop0).extrude(0.008145570638195357)
