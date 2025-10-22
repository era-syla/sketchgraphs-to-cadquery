import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02526, 0.09114).lineTo(-0.02126, 0.09114).lineTo(-0.02126, 0.04014).lineTo(-0.02526, 0.04014).lineTo(-0.02526, 0.09114).close()
solid=wp_sketch0.add(loop0).extrude(-0.01677632879091239)
