import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.028, -0.009).lineTo(0.0, -0.009).lineTo(0.0, 0.009).lineTo(0.028, 0.009).lineTo(0.028, -0.009).close()
solid=wp_sketch0.add(loop0).extrude(0.007687016186000037)
