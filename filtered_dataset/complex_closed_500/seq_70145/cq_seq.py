import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.024, 0.01968).lineTo(-0.02814, 0.00842).lineTo(-0.109, 0.03813).lineTo(-0.10486, 0.0494).lineTo(-0.024, 0.01968).close()
solid=wp_sketch0.add(loop0).extrude(-0.0210467957866141)
