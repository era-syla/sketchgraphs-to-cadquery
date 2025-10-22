import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.2125, 0.06887).lineTo(-0.0305, 0.06887).lineTo(-0.0305, 0.08977).lineTo(-0.2125, 0.08977).lineTo(-0.2125, 0.06887).close()
solid=wp_sketch0.add(loop0).extrude(-0.06304620712324181)
