import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02755, 0.01704).lineTo(0.02567, 0.01595).lineTo(0.02755, 0.01487).lineTo(0.02755, 0.01704).close()
solid=wp_sketch0.add(loop0).extrude(-0.005692019344658823)
