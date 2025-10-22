import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01675, 0.0012).lineTo(-0.02325, 0.0114).lineTo(-0.04555, 0.0114).lineTo(-0.04555, -0.02618).lineTo(0.04522, -0.02618).lineTo(0.04522, 0.0114).lineTo(0.02325, 0.0114).lineTo(0.01675, 0.0012).threePointArc((-0.0, 0.0), (-0.01675, 0.0012)).close()
solid=wp_sketch0.add(loop0).extrude(-0.16515163084986936)
