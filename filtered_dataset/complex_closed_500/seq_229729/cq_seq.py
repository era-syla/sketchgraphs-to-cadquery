import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.171, -0.14).lineTo(-0.171, -0.14).lineTo(-0.171, 0.14).lineTo(0.171, 0.14).lineTo(0.171, -0.14).close()
solid=wp_sketch0.add(loop0).extrude(-0.911508996163635)
