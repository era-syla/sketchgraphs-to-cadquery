import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05016, 0.00326).lineTo(-0.05016, 0.04147).lineTo(0.04247, 0.04147).lineTo(0.04247, 0.00299).lineTo(-0.05016, 0.00326).close()
solid=wp_sketch0.add(loop0).extrude(0.27017872844808366)
