import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02794, 0.00397).lineTo(0.02, 0.00397).lineTo(0.02, -0.00397).lineTo(0.02794, -0.00397).lineTo(0.02794, 0.00397).close()
solid=wp_sketch0.add(loop0).extrude(-0.008995494041723808)
