import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.006, 0.003).lineTo(-0.006, 0.00506).lineTo(-0.00495, 0.00506).threePointArc((-0.00557, 0.00408), (-0.006, 0.003)).close()
solid=wp_sketch0.add(loop0).extrude(0.004357625401078758)
