import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(2.0066, 0.45085).lineTo(2.0955, 0.45085).lineTo(2.0955, 0.05877).lineTo(2.0066, 0.05877).lineTo(2.0066, 0.45085).close()
solid=wp_sketch0.add(loop0).extrude(-0.4955314470904867)
