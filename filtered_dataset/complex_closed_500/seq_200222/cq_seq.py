import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02901, -0.02537).lineTo(-0.02901, -0.02537).lineTo(-0.02901, 0.02537).lineTo(0.02901, 0.02537).lineTo(0.02901, -0.02537).close()
solid=wp_sketch0.add(loop0).extrude(0.05919214610455836)
