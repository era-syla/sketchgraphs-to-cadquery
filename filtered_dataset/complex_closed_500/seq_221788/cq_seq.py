import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.57396, 0.0).lineTo(1.79316, 0.0).lineTo(1.79316, 0.2794).lineTo(0.57396, 0.2794).lineTo(0.57396, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(3.1450456100353272)
