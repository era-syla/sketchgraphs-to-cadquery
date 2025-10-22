import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.34925, 1.50411).lineTo(0.65405, 1.50411).lineTo(0.65405, 0.03391).lineTo(-0.34925, 0.03391).lineTo(-0.34925, 1.50411).close()
solid=wp_sketch0.add(loop0).extrude(-2.7644234730669175)
