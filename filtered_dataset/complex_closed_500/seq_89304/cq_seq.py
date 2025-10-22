import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.005, 0.0085).lineTo(0.006, 0.0085).lineTo(0.006, 0.0045).lineTo(0.01, 0.0045).lineTo(0.01, 0.00078).lineTo(0.01, -0.0085).lineTo(0.0055, -0.0085).lineTo(0.0055, 0.003).lineTo(0.003, 0.003).lineTo(0.003, -0.0085).lineTo(-0.01, -0.0085).lineTo(-0.01, -0.0065).threePointArc((-0.00561, 0.00411), (0.005, 0.0085)).close()
solid=wp_sketch0.add(loop0).extrude(0.025389816962856415)
