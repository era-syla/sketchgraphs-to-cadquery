import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(13.5, 8.5).lineTo(12.0, 8.5).lineTo(12.0, 10.5).lineTo(13.5, 10.5).lineTo(13.5, 8.5).close()
solid=wp_sketch0.add(loop0).extrude(3.2996491141655486)
