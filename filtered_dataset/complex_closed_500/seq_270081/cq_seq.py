import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04764, 0.02477).lineTo(-0.05589, 0.02477).lineTo(-0.05589, 0.01842).lineTo(-0.04764, 0.01842).lineTo(-0.04764, 0.02477).close()
solid=wp_sketch0.add(loop0).extrude(-0.008660598070239145)
