import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.35134, 6.63401).lineTo(-0.28829, 6.63401).lineTo(-0.28829, 6.60224).lineTo(-0.35134, 6.60224).lineTo(-0.35134, 6.63401).close()
solid=wp_sketch0.add(loop0).extrude(-0.148108101258595)
