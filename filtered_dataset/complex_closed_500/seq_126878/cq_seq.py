import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.21073, 0.00517).lineTo(0.21073, 0.21073).lineTo(0.00517, 0.21073).lineTo(0.00517, 0.00517).lineTo(0.21073, 0.00517).close()
solid=wp_sketch0.add(loop0).extrude(-0.41540062959052393)
