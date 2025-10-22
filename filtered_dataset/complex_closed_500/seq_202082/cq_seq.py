import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01041, 0.0).lineTo(0.00059, 0.0).lineTo(0.00059, 0.028).lineTo(-0.01041, 0.028).lineTo(-0.01041, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.06422062680814887)
