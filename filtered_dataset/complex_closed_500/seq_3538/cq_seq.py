import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.5334, 0.4445).lineTo(-0.5334, 0.4445).lineTo(-0.5334, -0.4445).lineTo(0.5334, -0.4445).lineTo(0.5334, 0.4445).close()
solid=wp_sketch0.add(loop0).extrude(1.9147209056149872)
