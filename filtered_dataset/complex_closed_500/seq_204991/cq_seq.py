import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05334, -0.09398).lineTo(0.26162, -0.09398).lineTo(0.26162, 0.15748).lineTo(-0.05334, 0.15748).lineTo(-0.05334, -0.09398).close()
solid=wp_sketch0.add(loop0).extrude(0.22828993717815688)
