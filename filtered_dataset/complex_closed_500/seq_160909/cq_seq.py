import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0762, 0.0).lineTo(0.0762, 0.0).lineTo(0.0762, 0.2032).lineTo(-0.0762, 0.2032).lineTo(-0.0762, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.07734293112385457)
