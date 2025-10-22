import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0, 0.31659).lineTo(-0.028, 0.31659).lineTo(-0.028, -0.19341).lineTo(0.0, -0.19341).lineTo(0.0, 0.31659).close()
solid=wp_sketch0.add(loop0).extrude(-1.1435556564526732)
