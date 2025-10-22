import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02134, 0.01388).lineTo(-0.02907, 0.01903).lineTo(-0.0335, 0.02199).lineTo(-0.0335, 0.00929).lineTo(-0.02907, 0.00929).lineTo(-0.02134, 0.00929).lineTo(-0.02134, 0.01388).close()
solid=wp_sketch0.add(loop0).extrude(-0.0207934987279197)
