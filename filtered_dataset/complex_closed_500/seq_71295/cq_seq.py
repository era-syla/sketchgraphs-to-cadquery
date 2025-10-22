import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.09525, -0.00159).lineTo(-0.09525, -0.00159).lineTo(-0.09525, 0.04921).lineTo(0.09525, 0.04921).lineTo(0.09525, -0.00159).close()
solid=wp_sketch0.add(loop0).extrude(-0.5055825733736237)
