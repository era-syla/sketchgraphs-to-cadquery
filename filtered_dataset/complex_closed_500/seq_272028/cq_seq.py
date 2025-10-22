import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01618, -0.00342).lineTo(-0.01618, -0.12845).lineTo(-0.01933, -0.13276).lineTo(-0.01933, -0.14215).lineTo(-0.00595, -0.15082).lineTo(-0.03234, -0.15082).lineTo(-0.03234, 0.02918).lineTo(-0.01618, -0.00342).close()
solid=wp_sketch0.add(loop0).extrude(0.3340036846616668)
