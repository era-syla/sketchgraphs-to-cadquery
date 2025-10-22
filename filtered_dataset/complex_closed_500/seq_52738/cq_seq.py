import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00764, 0.08211).lineTo(-0.00764, 0.05437).lineTo(0.06811, 0.05437).lineTo(0.06811, 0.08211).lineTo(0.05364, 0.08211).lineTo(0.05364, 0.06788).lineTo(0.04085, 0.06788).lineTo(0.04085, 0.08211).lineTo(0.02083, 0.08211).lineTo(0.02083, 0.06788).lineTo(0.00925, 0.06788).lineTo(0.00925, 0.08211).lineTo(-0.00764, 0.08211).close()
solid=wp_sketch0.add(loop0).extrude(-0.07396347323727158)
