import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04, 0.02151).lineTo(0.04, 0.02151).lineTo(0.04, -0.02151).lineTo(-0.04, -0.02151).lineTo(-0.04, 0.02151).close()
solid=wp_sketch0.add(loop0).extrude(-0.19399741017980654)
