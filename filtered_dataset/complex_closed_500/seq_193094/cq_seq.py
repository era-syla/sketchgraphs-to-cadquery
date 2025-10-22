import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02905, 0.0).lineTo(0.05888, 0.0).lineTo(0.05888, 0.06129).lineTo(0.02905, 0.06129).lineTo(0.02905, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.14975793434058823)
