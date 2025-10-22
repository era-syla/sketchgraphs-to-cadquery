import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0389, -0.0).lineTo(-0.0389, 0.02032).lineTo(-0.03382, 0.02032).lineTo(-0.03382, -0.02032).lineTo(-0.0389, -0.02032).lineTo(-0.0389, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.08262718719036993)
