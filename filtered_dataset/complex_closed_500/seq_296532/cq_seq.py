import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.381, 0.61681).lineTo(-0.381, 0.61681).lineTo(-0.381, 0.65491).lineTo(0.381, 0.65491).lineTo(0.381, 0.61681).close()
solid=wp_sketch0.add(loop0).extrude(-0.717754392258758)
